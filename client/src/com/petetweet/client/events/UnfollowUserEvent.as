// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class UnfollowUserEvent extends Event
	{
		public function UnfollowUserEvent(uid:String, bubbles:Boolean=true, cancelable:Boolean=false)
		{
			super("UnfollowUserEvent", bubbles, cancelable);
			
			this.uid = uid;
		}
		
		public var uid:String;
		
		override public function clone():Event {
			return new UnfollowUserEvent(uid);
		}
		
	}
}