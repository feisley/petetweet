// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class RegisterFailEvent extends Event
	{
		public function RegisterFailEvent(error:Object, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super("RegisterFailEvent", bubbles, cancelable);
			
			this.error = error;
		}
		
		public var error:Object;
		
		override public function clone():Event {
			return new RegisterFailEvent(error);
		}
		
	}
}