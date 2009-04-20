// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class RegisterFailEvent extends Event
	{
		public function RegisterFailEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super("RegisterFailEvent", bubbles, cancelable);
		}
		
		override public function clone():Event {
			return new RegisterFailEvent();
		}
		
	}
}